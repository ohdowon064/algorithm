import binascii
import os
import struct
import threading
import time
from multiprocessing import Process
from random import SystemRandom

_MAX_COUNTER_VALUE = 0xFFFFFF


class ObjectID:
    # 현재 프로세스 ID
    _pid = os.getpid()

    # 운영체제에서 생성하는 난수
    __random = os.urandom(5)

    # 카운터 초기값
    _inc = SystemRandom().randint(0, _MAX_COUNTER_VALUE)

    # 카운터 증분 락킹
    _inc_lock = threading.Lock()

    @classmethod
    def _random(cls):
        pid = os.getpid()
        if pid != cls._pid:
            cls._pid = pid
            cls.__random = os.urandom(5)
        return cls.__random

    def __init__(self):
        # 4bytes timestamp
        # >: 빅인디안
        # I: unsigned int
        # struct.pack: 파이썬 객체를 bytes로 변환하는 함수 (반대는 unpack)
        object_id = struct.pack(">I", int(time.time()))

        # 5bytes 고유 랜덤값
        object_id += self._random()

        # 3bytes 카운터
        with self._inc_lock:
            object_id += struct.pack(">I", self._inc)[1:4]
            # 카운터 1 증가
            ObjectID._inc = (ObjectID._inc + 1) % (_MAX_COUNTER_VALUE + 1)

        self.__id = object_id

    def __str__(self):
        return binascii.hexlify(self.__id).decode()

    def __repr__(self):
        return f"ObjectId('{str(self)}')"

    def __eq__(self, other):
        if isinstance(other, ObjectID):
            return self.__id == other.__id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__id)


def oid_test(p_name):
    print(f"{p_name} pid >>> {os.getpid()}")
    print(f"{p_name} >>> 테스트 시작")
    A = ObjectID()
    B = ObjectID()
    C = A
    D = ObjectID()
    print(f"{p_name} >>> A = {A}, B = {B}, C = {C}, D = {D}")
    print(f"{p_name} >>> A == B: {A == B}, A == C: {A == C}")

    documents = {
        A: {"name": "오도원", "age": 26},
        B: {"name": "오도투", "age": 28},
        D: {"name": "오도쓰리", "age": 27}
    }

    print(f"{p_name} >>>", documents)
    print(f"{p_name} >>> 테스트 종료")
    print()


if __name__ == "__main__":
    for i in range(4):
        p = Process(target=oid_test, args=(f"p{i + 1}",))
        p.start()
        p.join()
