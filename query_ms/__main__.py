import redis


if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)

    key, val = 'c', 'true'
    print(f'setting {key}={val}')
    print(r.set(key, val))

    assert(r.get(key).decode('utf-8') == val)
    print("redis connection works.")


