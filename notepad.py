# برای ایجاد فایل متنی و خواندن متن هایی که از قببل نوشته بودیم
def load_notes(personal):
    notes = []
    try:
        with open(personal, "r", encoding="utf-8") as file:
            for line in file:
                notes.append(line.strip())
    except FileNotFoundError:
        pass
    return notes
#==================================================
# برای نوشتم و ذخیره کردن درون فایل
def save_notes(personal, notes):
    with open(personal, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")
#==================================================
# برای نمایش متن های تکست
def show_notes(notes):
    if not notes:
        print("you don't have note !") # یادداشتی وجود ندارد.
    else:
        print("your nots :") # یادداشت‌های شما:
        # enumerate() یه تابع داخلی پایتونه که وقتی داری روی یه لیست یا هر شیء قابل تکرار (iterable) حلقه می‌زنی، بهت هم اندیس (شماره خط) رو میده و هم مقدار اون خط.
        # idx اینجا یک متغیر معمولیه که توی این حلقه  for بهش نقش شماره یادداشت داده شده
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note}")
#==================================================
# برای اضافه کردن به یادداشت ها
def add_note(notes):
    note = input("enter your new note :") # متن یادداشت جدید را وارد کنید:
    notes.append(note)
    print("COMPLITED") # تکمیل شد 
#==================================================
# برای پاک کردن یادداشت ها
def delete_note(notes):
    show_notes(notes)
    if notes:
        try:
            num = int(input("Enter the number of the note you want to delete :")) # شماره یادداشتی که می‌خواهید حذف کنید را وارد کنید: 
            if 1 <= num <= len(notes):
                removed = notes.pop(num - 1)
                print(f"note '{removed}' deleted.")
            else:
                print("You did not enter a valid number.") # شماره معتبر وارد نکردید
        except ValueError:
            print("please enter a number. ") # لطفاً یک عدد وارد کنید.
#==================================================
#
def main():
    filename = "personal.txt"
    notes = load_notes(filename)

    while True:
        print("--------------------")
        print("--------------------")
        print("---note pad---\n") # --- دفترچه یادداشت ---
        print("1. show notes") # نمایش یادداشت‌ها
        print("2. new note") #  افزودن یادداشت
        print("3. delet note") # حذف یادداشت
        print("4. exit") #خروج
        choice = input("enter your choice : ") #انتخاب خود را وارد کنید:

        if choice == "1":
            show_notes(notes)
        elif choice == "2":
            add_note(notes)
            save_notes(filename, notes)
        elif choice == "3":
            delete_note(notes)
            save_notes(filename, notes)
        elif choice == "4":
            print("sayonara")
            break
        else:
            print("The option is invalid. Please try again.") # گزینه نامعتبر است. دوباره تلاش کنید.
#==================================================
#
if __name__ == "__main__":
    main()