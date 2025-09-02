#========================================================
import zipfile
import string
import itertools

# مسیر فایل زیپ رمزدار
zip_path = "Microsoft.NET.Framework.4.8.0.Build.4115.Final.x86.x64_YasDL.com.zip"

# ایجاد لیستی از حروف a-z و اعداد 1-9
letters = list(string.ascii_lowercase)
numbers = list("123456789")
characters = letters + numbers

# باز کردن فایل زیپ
with zipfile.ZipFile(zip_path) as zf:
    found = False

    # طول رمز رو محدود به 1 تا 4 کاراکتر فرض می‌کنیم (برای سرعت)
    for length in range(1, 5):
        for guess in itertools.product(characters, repeat=length):
            password = ''.join(guess)
            try:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                print("✅ رمز پیدا شد:", password)
                found = True
                break
            except:
                print("❌ امتحان شد:", password)
        if found:
            break

    if not found:
        print("🚫 رمز پیدا نشد.")
