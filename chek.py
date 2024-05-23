import requests
import time

def check_username(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(f"رد الموقع لاسم المستخدم {username}: {response.status_code} (مستخدم)")
            return f"اسم المستخدم {username} مستخدم."
        elif response.status_code == 404:
            print(f"رد الموقع لاسم المستخدم {username}: {response.status_code} (متاح)")
            return f"اسم المستخدم {username} متاح."
        else:
            print(f"رد الموقع لاسم المستخدم {username}: {response.status_code} (غير معروف)")
            return f"لم يتمكن من فحص اسم المستخدم {username}. الحالة: {response.status_code}"
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال لاسم المستخدم {username}: {e}")
        return f"حدث خطأ أثناء محاولة فحص اسم المستخدم {username}: {e}"

def main():
    with open('usernames.txt', 'r', encoding='utf-8') as file:
        usernames = file.readlines()
    
    usernames = [username.strip() for username in usernames]
    
    for username in usernames:
        result = check_username(username)
        print(result)
        time.sleep(2)  # الانتظار لمدة 2 ثانية بين الطلبات لتجنب الحظر

if __name__ == "__main__":
    main()