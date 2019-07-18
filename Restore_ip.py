class Solution(object):



    def make_combinations(self, min_num, max_num):

        '''
        returns a list of list.

        input 
        min_num = 1
        max_num = 4

        output: [[1,1,1,1], [1,1,1,2]........[3,3,3,2], [3,3,3,3]]

        '''

        combinations = list()
        for i in range(min_num, max_num):
            for j in range(min_num, max_num):
                for k in range(min_num, max_num):
                    for l in range(min_num, max_num):
                        combinations.append([i, j, k, l])
        return combinations

    def make_combinations_test(self):

        print "make_combinations_test...."
        assert 81 == len(self.make_combinations(1,4))
        assert [[1,1,1,1], [1,1,1,2]] == sorted(self.make_combinations(1,4))[:2]
        assert [[3,3,3,2], [3,3,3,3]] == sorted(self.make_combinations(1,4))[-2:]

    def combination_sum_equal_length(self, total, combination):

        '''
        return if length equals the sum of the numbers
        in the combination list

        for test cases refer combination_equal_length_test
        '''
        sum_of_combination = 0
        for i in combination:
            sum_of_combination += i
        if sum_of_combination == total:
            return True
        else:
            return False

    def combination_equal_length_test(self):

        assert True == self.combination_sum_equal_length(4, [1,1,1,1])
        assert False == self.combination_sum_equal_length(5, [1,1,1,1])
        assert True == self.combination_sum_equal_length(0, [0,0,0,0])


    def get_combinations_for(self, total, min_num, max_num):
        '''
        takes a total and a range.. min_num, max_num
        returns a list of list where each list sum up to
        the total

        for test case refer to get_combinations_for_test
        '''

        combinations_for_length = list()
        combinations = self.make_combinations(min_num, max_num)
        for combination in combinations:
            if self.combination_sum_equal_length(total, combination):
                combinations_for_length.append(combination)
        return combinations_for_length

    def get_combinations_for_test(self):

        print "testing get_combinations_for_test......"
        assert [[1,1,1,1]] == self.get_combinations_for(4, 1, 4)
        assert [[1,1,1,2], [1,1,2,1], [1,2,1,1], [2,1,1,1]] == self.get_combinations_for(5, 1, 4)


    def valid_ip_digit(self, strng):
        '''
        the string must be between 0 and 255
        '''
        return 0 <= int(strng) <=255

    def leading_zeros(self, strng):
        '''
        checks if a string has leading zeros

        for test cases refer leading_zeros_test
        '''

        if strng.startswith("0") and len(strng) > 1:
            return False
        else:
            return True  

    def leading_zeros_test(self):

        print "leading_zeros_test.."
        assert False == self.leading_zeros("001")
        assert True == self.leading_zeros("0")
        assert False == self.leading_zeros("00")
        assert False == self.leading_zeros("010")
        assert True == self.leading_zeros("100")

    def make_ip_from_a_combination(self, s, combination):

        '''
        takes a string and list (combination)
        the numbers in the list correspond to the
        number of digits in a ip address number 
        preceding the dot(".")

        for test cases refer make_ip_from_a_combination_test
        '''

        lower_bound = 0
        str_list = list()
        upper_bound = 0
        for c in combination:
            upper_bound += c
            ip_num_as_str = s[lower_bound:upper_bound]
            if self.valid_ip_digit(ip_num_as_str) and self.leading_zeros(ip_num_as_str):
                str_list.append(ip_num_as_str)
            else:
                return None
            lower_bound += c
        return ".".join(str_list)

    def make_ip_from_a_combination_test(self):

        print "make_ip_from_a_combination_test..."
        assert "1.1.1.1" ==  self.make_ip_from_a_combination("1111", [1,1,1,1])
        assert "192.1.1.0" == self.make_ip_from_a_combination("192110", [3,1,1,1])
        assert None == self.make_ip_from_a_combination("2562255255", [3,1,3,3])

    def string_to_ip(self, s):
        '''
        takes a string and returns valid
        IP addresses

        for test cases refer string_to_ip_test
        '''
        combinations = self.get_combinations_for(len(s), 1, 4)
        ips = list()
        for c in combinations:
            ip = self.make_ip_from_a_combination(s, c)
            if ip:
                ips.append(ip)
        return ips


    def string_to_ip_test(self):

        print "string_to_ip_test...."
        assert ["1.1.1.1"] == self.string_to_ip("1111")
        assert sorted(["1.2.1.11", "1.2.11.1", "1.21.1.1", "12.1.1.1"]) == sorted(self.string_to_ip("12111"))


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # checking an edge case a valid IP address 
        # cannot have less than 4 digits or more 
        # than 12 digits
        if 4 <= len(s) <= 12:
            return self.string_to_ip(s)
        return []

    def restoreIpAddresses_test(self):
        print "testing restoreIpAddresses_test......"
        assert [] == self.restoreIpAddresses("111")
        assert ["255.255.11.135", "255.255.111.35"] == self.restoreIpAddresses("25525511135")

def main():
    s = Solution()
    s.make_combinations_test()
    s.combination_equal_length_test()
    s.get_combinations_for_test()
    s.make_ip_from_a_combination_test()
    s.string_to_ip_test()
    s.leading_zeros_test()
    s.restoreIpAddresses_test()

main()
        