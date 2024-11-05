import re
import pickle


# Потенциально уязвимое регулярное выражение для ReDoS
pattern = r"(a+)+"
re.match(pattern, "aaaaaaaaaaaaaaaaaaaaaaaa!")

# ======================================================================================================================

# Example 1: This should match both the old and new patterns
# Vulnerable deserialization of untrusted data
def insecure_function(data):
    # Insecure deserialization with untrusted data
    return pickle.loads(data)

# Example 2: This should match only the old pattern, not the new one
# Defining a variable with the keyword "loads" but not actually using it
loads = "This should not trigger the new pattern but might in the old one."

# Example 3: Safe usage with a predefined trusted data source (should not match the new pattern)
def safe_function():
    trusted_data = b'\x80\x03K\x01.'  # Example of serialized data
    return pickle.loads(trusted_data)  # Safe: predefined trusted data

# Example 4: Usage of the keyword in a comment (should be ignored in the new pattern)
# "pickle.load()" mentioned in a comment for documentation purposes
# Example: pickle.load(<file>) - for demonstration only

# Example 5: A dictionary key using the term 'deserialize' (should not match the new pattern)
config = {
    "deserialize_method": "pickle.loads"  # Should not trigger the new pattern
}

# Example 6: Actual vulnerable code that should match the new pattern
def deserialize_user_data(user_data):
    # Vulnerable deserialization of user data
    return pickle.loads(user_data)

# Execution for testing purposes
insecure_function(b'')   # Expected to be caught by both patterns
safe_function()          # Expected to be ignored by the new pattern
deserialize_user_data(b'')  # Expected to be caught by the new pattern

# ======================================================================================================================

# TODO: example "to do" for scaning
some_code = 'test code for "to do"'
if "to do" in some_code:
    a = 'my "to do" found"'

# TODO: example commented code "to do" for scaning
# some_commented_code = 'test commented code for "to do"'
# if "to do" in some_commented_code:
#   a = 'my "to do" found"'
# 123.0.0.1
# 223.0.0.1
# 123.3.0.1
# 125.0.0.1

api_server = "192.168.1.4"  # IP for API server
db_host = "10.0.0.4"  # Database IP
# Backup server IP: 172.16.0.4

db_host1 = "text 10.0.0.4"  # Database IP
db_host2 = "s 10.0.0.4"  # Database IP
db_host3 = "ss 10.0.0.4 123"  # Database IP


# ======================================================================================================================

ssh_key = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr7zVJ6aO0t3bD/yhC67hjN4dL5pk0Yg/5K4iM7LV67DdOi4zNySHFHbEvOiwVljYp9DjU9x8Ys14U8xzL3a5z7IR9QiKT9m3fjbRVGT3Zz/57f6mhU6xE9Y3kTbksb5y0PL2vL2OvAxlM93eH87uYyHgMeTHpKs0m2Gj8yJhR3Nh4n7F8ItIHr2sOQxnnXW9P+DLrmWaFFMyMkKzNzX/sBHvV test@host"
my_ssh_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr7zVJ6aO0t3bD/yhC67hjN4dL5pk0Yg/5K4iM7LV67DdOi4zNySHFHbEvOiwVljYp9DjU9x8Ys14U8xzL3a5z7IR9QiKT9m3fjbRVGT3Zz/57f6mhU6xE9Y3kTbksb5y0PL2vL2OvAxlM93eH87uYyHgMeTHpKs0m2Gj8yJhR3Nh4n7F8ItIHr2sOQxnnXW9P+DLrmWaFFMyMkKzNzX/sBHvV test@host'

api_key = '1hD4O7A9OgdjhP4lRgGzX9Q6UvY3Ht5vZs6H2Jr'
my_api_key = "1hD4O7A9OgdjhP4lRgGzX9Q6UvY3Ht5vZs6H2Jr"

passwd = "V3q#5mZyT&8LrN2b"
my_password = 'p9T@G6uLx!7Ow4Ns'
my_passwd_secrets = "S6kV@dR9q$1JmW8x"
password_of_server = 'X2pLm!8Nz4u#Q7Ks'

