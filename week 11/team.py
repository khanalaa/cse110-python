
# max_num = 0
# max_book = ""
# with open("books_and_chapters.txt") as f:
#     for line in f:
#         clean_line = line.strip()
#         data = clean_line.split(":")
#         name = data[0]
#         chapter =  int(data[1])
#         book_name = data[2]
#         print(f"Scripture: {book_name}, Book: {name}, Chapters: {chapter}")

#         if chapter > max_num:
#             max_num = chapter
#             max_book = book_name
    
#     print(f"\nThe largest number of chapters is {max_num}.")
#     print(f"The book with the largest number of chapter is {max_book}.")


largest_chap = 0
largest_name = ''

book_input = input("Which volume of scriptures would you like to learn about: ").lower()
print()
with open("books_and_chapters.txt") as f:
    for line in f:
        clean_line = line.strip()
        data = clean_line.split(":")
        name = data[0]
        chapter =  int(data[1])
        book_name = data[2].lower()

    #     if book_name == "Book of Mormon":
    #        print(f"Scripture: {book_name}, Book: {name}, Chapters: {chapter}")

    #     if book_name ==  "Book of Mormon" and chapter > largest_chap:
    #         largest_chap = chapter
    #         largest_name = name

    # print(f"\nThe book with largest numbers of chapters is {largest_chap} in {largest_name}")        
                
        if book_name == book_input and chapter > largest_chap:
            largest_chap = chapter
            largest_name = name
    print(f"The largest number of chapters in {book_input} is {largest_chap}")


            
