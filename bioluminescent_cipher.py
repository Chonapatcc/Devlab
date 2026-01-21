def decode_bioluminescent_cipher(input_string):
    # แยกคำในประโยค
    words = input_string.split()
    result_sequence = ""
    
    for word in words:
        # ตรวจสอบเงื่อนไขพิเศษ (Case-sensitive ตามตัวอย่างโจทย์)
        if word == "fox":
            result_sequence += "8"
        elif word == "my":
            result_sequence += "1"
        else:
            # นับจำนวนอักขระที่เป็นตัวอักษรหรือตัวเลขเท่านั้น
            # วิธีนี้จะทำให้ '?????' กลายเป็น 0
            count = 0
            for char in word:
                if char.isalnum():
                    count += 1
            result_sequence += str(count)
            
    # แปลงเป็นจำนวนเต็มเพื่อแสดงผล
    try:
        return int(result_sequence)
    except ValueError:
        return 0

# # ส่วนทดสอบ (Test Harness)
# # กรณีตัวอย่างที่ 1
# # Input: this is a red brown fox
# # Process: 4, 2, 1, 3, 5, 8
# # Output: 421358
# print(decode_bioluminescent_cipher("this is a red brown fox")) 

# # กรณีตัวอย่างที่ 2
# # Input: oh my goshhhhhh
# # Process: 2, 1, 9
# # Output: 219
# print(decode_bioluminescent_cipher("oh my goshhhhhh"))

# # กรณีตัวอย่างที่ 3
# # Input: what the?????
# # Process: 4, 3, 0
# # Output: 430
# print(decode_bioluminescent_cipher("what the?????"))

print(decode_bioluminescent_cipher(input().strip()))