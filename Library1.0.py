from datetime import datetime, timedelta

class Library:
    member_counter = 1000
    book_counter = 1000
    
    def __init__(self):
        #=====BOOKS=====
        self.books = {}                             # {book_id: {Title, author, available}}
        #=====MEMBERS=====
        self.members = {}                     # {member_id: {name, age, borrowed_books, borrow_limit, borrow_history}}
        #=====BORROW=====
        self.borrowed_history = {}      # {(member_id, book_id): {borrow_date, return_date}}
        
#========== BOOK METHODS ==========
    def add_books(self, Title ,Author): 
        """
            اضافه کردن کتاب
            آی دی کتاب خودکار از 1000 شماره گذاری میکنه 
        """
        book_id = Library.book_counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        Library.book_counter += 1
        self.books[book_id] = {"Title": Title, "Author": Author, "Available": True}
        print(f"Book Added: ID = {book_id}, Title = '{Title}',  Author = {Author}")
        return book_id

    def delete_books(self, book_id): 
        """
            حذف کتاب
        """
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book {book_id} deleted!")
        else:
            print("Book not found!")

    def show_books(self):
        """
            b_id = شناسه/کلید کتاب 
            info = مقدار و اطلاعات کتاب{ "Title": ..., "Author": ..., "Available": ... }
        """
        print("\nBooks List:")
        if not self.books:
            print("No books in library yet.")
            return
        for b_id, info in self.books.items():
            status = "Available" if info["Available"] else "Borrowed"
            print(f"ID: {b_id}, Title: {info['Title']}, Author: {info['Author']}, Status: {status}")

    def search_books(self, keyword):
        """
            book_id = شناسه/کلید کتاب 
            book = مقدار و اطلاعات کتاب{ "Title": ..., "Author": ..., "Available": ... }
        """
        found = False
        for book_id, book in self.books.items():
            if keyword.lower() in book["Title"].lower():
                status = "Available ✅" if book["Available"] else "Borrowed ❌"
                print(f"Found book ID: {book_id}, Title: {book['Title']}, Author: {book['author']}, Status: {status}")
                found = True
        if not found:
            print("No book found with this keyword.")

#========== MEMBER METHODS ==========
    def add_member(self, name, age=None):
        """
            اضافه کردن عضو
        """
        member_id = Library.member_counter
        Library.member_counter += 1
        self.members[member_id] = {
            "name": name,
            "age": age,
            "borrowed_books": [],   # لیست کتاب‌های قرضی
            "borrow_limit": 3,         # محدودیت امانت
            "borrow_history": []     #تاریخچه کتاب های قرضی
            }
        print(f"Member added: ID = {member_id}, Name = {name}, Age = {age}")
        return member_id

    def delete_member(self, member_id):
        """
            حذف کردن عضو
        """
        if member_id in self.members:
            del self.members[member_id]
            print(f"Member {member_id} deleted! ✅")
        else:
            print("Member not found! ❌")

    def show_members(self):
        """
            member_id = شناسه/کلید کتاب 
            info = مقدار و اطلاعات کتاب{ "Title": ..., "author": ..., "Available": ... }
        """
        print("\nMembers List:")
        if not self.members:
            print("No members yet.")
            return
        for member_id, info in self.members.items():
            print(f"ID: {member_id}, Name: {info['name']}, Age: {info['age']}, Borrowed Books: {len(info['borrowed_books'])}/{info['borrow_limit']}")

    def change_member_info(self, member_id, new_name=None, new_limit=None):
        """
            تغییر اطلاعات اعضا
        """
        if member_id not in self.members:
            print("Member not found! ❌")
            return
        member = self.members[member_id]
        if new_name:
            member["name"] = new_name
        if new_limit:
            member["borrow_limit"] = new_limit
        print(f"Member {member_id} updated successfully! ✏️")

#========== BORROW & RETURN METHODS ==========  
    def lend_book(self, member_id, book_id):
        """
            قرض دادن کتاب با مهلت 14 روزه
        """
        if member_id not in self.members:
            print("Member not found! ❌")
            return
        if book_id not in self.books:
            print("Book not found! ❌")
            return
        member = self.members[member_id]
        book = self.books[book_id]

        if not book["Available"]:
            print(f"Book '{book['Title']}' is already borrowed! 📚 ")
            return
        if len(member["borrowed_books"]) >= member["borrow_limit"]:
            print(f"Member {member_id} has reached the borrow limit!")
            return
        
        # Borrow process
        book["Available"] = False
        member["borrowed_books"].append(book_id)
        borrow_date = datetime.now()
        return_date = borrow_date + timedelta(days=14)
        member["borrow_history"].append({"book_id": book_id, "borrow_date": borrow_date, "return_date": return_date})
        self.borrowed_history[(member_id, book_id)] = {"borrow_date": borrow_date, "return_date": return_date}
        print(f"Book '{book['Title']}' lent to Member {member_id} until {return_date.date()} ✅")

    def return_book(self, member_id, book_id):
        """
            بازگشت کتاب و اعلام تاخیر
        """
        if (member_id, book_id) not in self.borrowed_history:
            print("This book was not borrowed by this member!")
            return
        book = self.books[book_id]
        member = self.members[member_id]

        # Return process
        book["Available"] = True
        if book_id in member["borrowed_books"]:
            member["borrowed_books"].remove(book_id)
        borrow_info = self.borrowed_history.pop((member_id, book_id))
        today = datetime.now()
        if today > borrow_info["return_date"]:
            delay_days = (today - borrow_info["return_date"]).days
            print(f"Book '{book['Title']}' returned with {delay_days} day(s) delay!")
        else:
            print(f"Book '{book['Title']}' returned on time by Member {member_id} ✅")

    def books_on_loan(self):
        """
            (m_id, b_id) کلید واژه کتاب و عضو
            info مقدار و اطلاعات کتاب 
        """
        print("\nBooks Currently on Loan:")
        if not self.borrowed_history:
            print("No books currently on loan.")
            return
        for (m_id, b_id), info in self.borrowed_history.items():
            print(f"Book ID: {b_id}, Member ID: {m_id}, Return Date: {info['return_date'].date()}")

    def delay_check(self, member_id):
        """
            بررسی تاخیر و ذخیره درون یک لیست
        """
        if member_id not in self.members:
            print("Member not found!")
            return
        member = self.members[member_id]
        now = datetime.now()
        delayed_books = []
        for book_id in member["borrowed_books"]:
            for record in member["borrow_history"]:
                if record["book_id"] == book_id and now > record["return_date"]:
                    delayed_books.append({"book_id": book_id, "days_late": (now - record["return_date"]).days})
        return delayed_books

    def late_penalty(self, member_id, daily_fine=10000):
        """
            اعمال جریمه دیرکرد
        """
        delays = self.delay_check(member_id)
        if not delays:
            print("No late books.")
            return 0
        total_fine = sum(d["days_late"] * daily_fine for d in delays)
        print(f"Total late penalty for Member {member_id}: {total_fine} 💰")
        return total_fine

# ==========REPORT METHODS ==========    
    def popular_books(self):
        """
            m_id = کلید واژه عضو
            member اطلاعات عضو
            شمارش تعداد  دفعات ذخیره کتاب
            نمایش تعداد دفعات قرض گرفتن کتاب و محبوبیت اون بر اساس دفعات قرض گرفته شده
        """
        borrow_count = {}
        for m_id, member in self.members.items():
            for record in member["borrow_history"]:
                book_id = record["book_id"]
                borrow_count[book_id] = borrow_count.get(book_id, 0) + 1
        if not borrow_count:
            print("No borrow history yet.")
            return
        sorted_books = sorted(borrow_count.items(), key=lambda x: x[1], reverse=True)
        print("\nPopular Books:")
        for book_id, count in sorted_books:
            print(f"{self.books[book_id]['Title']} -> Borrowed {count} times")

    def monthly_report(self):
        """
            گزارش ماهانه وثبت تعداد کتابهای قرض گرفته شده در ماه
        """
        current_month = datetime.now().strftime("%Y-%m")
        count = 0
        for m_id, member in self.members.items():
            for record in member["borrow_history"]:
                if record["borrow_date"].strftime("%Y-%m") == current_month:
                    count += 1
        print(f"\n📅 Monthly report: {count} books borrowed this month.")


# ========== TEST ==========

if __name__ == "__main__":
    lib = Library()

    # Add books
    b1 = lib.add_books("Power of Silence", "Susan Cain")
    b2 = lib.add_books("You Can't Hurt Me", "David Goggins")
    print("====================")

    # Add member
    m1 = lib.add_member("persian.ghost", 20)
    print("====================")

    # Lend books
    lib.lend_book(m1, b1)
    lib.lend_book(m1, b2)
    print("====================")

    # Show
    lib.show_books()
    print("====================")
    lib.show_members()
    lib.books_on_loan()
    print("====================")

    # Return book
    lib.return_book(m1, b1)
    lib.books_on_loan()
    print("====================")

    # Popular & report
    lib.popular_books()
    print("====================")
    lib.monthly_report()
    print("====================")
