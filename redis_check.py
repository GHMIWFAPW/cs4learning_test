import datetime
import redis
# 以抽帧时间为准的判断违规打标次数 [draw_time是个strftime，需要转化]
def draw_check(redis, key, draw_time, window=60, limit=5):
    """ 查询key在有效时间区间内的次数[需要保证KAFKA进入的数据按照时间有序]
    :param redis: Redis客户端
    :param key: Redis用于保持计数器的主键===> [teacher_id; room_id; label(ai_img_porn_label; ai_img_class; ali_is_same_person)]
    :param window: Rolling时间窗口[单位为秒]
    :param limit: 阈值
    :param draw_time: 事务发生时间
    :return: 指定时间窗口内到达最大限制值时，为真
    """
    # 抽帧时间转化为数字时间
    draw_time = datetime.datetime.timestamp(datetime.datetime.strptime(draw_time, "%Y-%m-%d %H:%M:%S"))
    # 获得现在时间相比于其他时间的差值
    expires = draw_time - window
    redis.zremrangebyscore(key, '-inf', expires)
    # 将数据按照某个时间插入，显然，应该是事务发生时间[key在事务时间发生，则在这个位置存入这个时间]
    redis.zadd(key, {draw_time:draw_time})
    # 基于给定的限制，判断主键数据是否超越[返回的是key所拥有的总数(同时因为删除了有效时间之外的数据，故而只有截止到现在为止的数据次数)]
    if redis.zcard(key) >= limit:
        return True
    return False


# 判断此条违规数据总数是否达标[用于REDIS建立时间时的统计]
def check(redis, key, window=1, limit=5):
    """ 查询key是否有效；若有效,则次数+1,且重新设置其有效时间；否则若无效，则设置其有效且次数为1. 最后返回判断结果，此条数据是否
    :param redis: Redis客户端
    :param key: Redis用于保持计数器的主键===> [teacher_id; room_id; ai_img_porn_label; ai_img_class; ali_is_same_person]
    :param window: Rolling时间窗口[单位为分钟]
    :param limit: 阈值
    :return: 指定时间窗口内到达最大限制值时，为真
    """
    # 如果主键有效,则对其值+1,并重新设置有效期以及数值
    if redis.exists(key) > 0:
        current_value = int(str(r.get(key), 'utf-8')) + 1
        redis.setex(key, timedelta(minutes=window), value=current_value)
    # 否则主键无效，则将其设置为1，并重新设置有效期【因为凡是能出发检测的，都是触发规则的】
    else:
        current_value = 1
        redis.setex(key, timedelta(minutes=window), value=current_value)
    # 判定是否达到上限
    if current_value >= limit:
        return True
    return False
