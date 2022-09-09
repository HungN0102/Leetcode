# Input: cpdomains = ["9001 discuss.leetcode.com"]
# Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
# Explanation: We only have one website domain: "discuss.leetcode.com".
# As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times


class Solution(object):
    def subdomainVisits(self, cpdomains):
        hashmap = {}
        for domain in cpdomains:
            count = domain.split(" ")[0]
            count = int(count)

            domains = domain.split(" ")[1].split(".")

            currentDomain = []
            for d in reversed(domains):
                currentDomain.append(d)
                currentString = ".".join(reversed(currentDomain))

                if currentString not in hashmap:
                    hashmap[currentString] = 0
                hashmap[currentString] += count

        return ["{} {}".format(hashmap[x], x) for x in hashmap]