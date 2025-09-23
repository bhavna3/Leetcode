class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vr1=version1.split('.')
        vr2=version2.split('.')

        n=max(len(vr1),len(vr2))

        while (len(vr1)!=n):
            vr1.append(0)

        while (len(vr2)!=n):
            vr2.append(0)

        for i in range(n):
            v1=int(vr1[i])
            v2=int(vr2[i])

            if v1<v2:
                return -1
            elif v1>v2:
                return 1
        return 0
        