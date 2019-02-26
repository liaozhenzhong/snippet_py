class Solution:
    def clean_address(self, email):
        local_name, domain_name = email.split('@')
        local_name = local_name.split('+')[0]
        local_name = local_name.replace('.', '')
        return local_name, domain_name

    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        clean_email = set()
        for email in emails:
            local_name, domain_name = self.clean_address(email)
            clean_email.add((local_name, domain_name))
        return len(clean_email)

def test_unique_email_address():
    so = Solution()
    assert so.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2

