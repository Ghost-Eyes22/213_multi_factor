# a213_multi_factor.py
import multifactorcli as mfc

# create a multi-factor interface to a restricted app
my_auth = mfc.MultiFactorAuth()

# set the users authentication information
question = "whats your favorite one piece character?"
answer = "Law"
my_auth.set_multiFactorAuthentication(question, answer)

username= ""
password = ""

my_auth.run()