import sys
input = sys.stdin.readline  # 더 빠른 입력 처리

M = int(input())
class SetOperations:
    def __init__(self):
        self.S = set()

    def add(self, x):
        self.S.add(x)  # 1-20 범위 체크 제거 (문제에서 보장된다면)
    def remove(self, x):
        self.S.discard(x)
    def check(self, x):
        print(1 if x in self.S else 0)  # 직접 출력
    def toggle(self, x):
        if x in self.S:
            self.S.remove(x)
        else:
            self.S.add(x)
    def all(self):
        self.S = set(range(1,21))
    def empty(self):
        self.S.clear()  # set() 대신 clear() 사용

set_ops = SetOperations()
for _ in range(M):
    cmd, *arg = input().split()
    if arg:  # 인자가 있는 경우
        x = int(arg[0])
        if cmd == 'add': set_ops.add(x)
        elif cmd == 'remove': set_ops.remove(x)
        elif cmd == 'check': set_ops.check(x)
        elif cmd == 'toggle': set_ops.toggle(x)
    else:  # all, empty 명령
        if cmd == 'all': set_ops.all()
        else: set_ops.empty()