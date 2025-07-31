from login_helper import is_valid_username, is_valid_password

def test_valid_username():
    assert is_valid_username('testuser123')  
    assert not is_valid_username("hi")       
    assert not is_valid_username("abcde")   
    assert not is_valid_username("test_user") 

def test_valid_password():
    assert is_valid_password('ABCDEFGHIJK')   
    assert not is_valid_password('PASSWRD')  
    
def test_regression_inputs():
    assert is_valid_username("user1234")      
    assert is_valid_password("PASSWORD")     
