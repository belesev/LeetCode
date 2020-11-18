from typing import List

class Solution:
    def __restore_ips(self, result_set: List[str], s, segments_count, prefix: str):
        # finalization: check whether this leaf of the tree is not valid, then return
        # if valid, add to the result set
        if len(s) == 0:
            return

        if segments_count == 1:
            if not self.__is_valid(s):
                return
            result = prefix + "." + s
            result_set.append(result)
            return

        # if segments_count > 1, choose the length for the next one
        for current_segment_length in range(1, min(3, len(s))+1):
            current_segment = s[0:current_segment_length]
            if not self.__is_valid(current_segment):
                continue

            if len(prefix):
                new_prefix = prefix + "." + current_segment
            else:
                new_prefix = current_segment

            # recursive call for the substring and decreased segments_count
            self.__restore_ips(result_set, s[current_segment_length:], segments_count - 1, new_prefix)

    @staticmethod
    def __is_valid(s: str):
        if len(s) > 3:
            return False
        # no leading zeros
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        result_set = list()
        self.__restore_ips(result_set, s, 4, "")
        return result_set
