import math

def encrypt_square_code(message):
    trim_msg = message.replace(" ", "")
    array_of_trim_msg = list(trim_msg)
    
    n = len(trim_msg)
    n_row = round(pow(n, 0.5))
    n_col = math.ceil(n / n_row)

    matrix_of_char = [array_of_trim_msg[i:i+n_col] for i in range (0, len(array_of_trim_msg), n_col)]

    encrypted_msg = [''] * n_col
    for i in range (len(matrix_of_char)):
        for j in range(len((matrix_of_char[i]))):
            encrypted_msg[j] += matrix_of_char[i][j]
    print(' '.join(encrypted_msg))
    return ' '.join(encrypted_msg)

def decrypt_square_code(message):
    trim_msg = message.split()
    n_row = len(trim_msg)
    
    matrix_of_char = []
    for i in range (len(trim_msg)):
        matrix_of_char.append(list(trim_msg[i]))

    n_col = len(matrix_of_char[0])

    decrypted_msg = [''] * n_col
    for i in range (len(matrix_of_char)):
        for j in range(len((matrix_of_char[i]))):
            decrypted_msg[j] += matrix_of_char[i][j]
    print(''.join(decrypted_msg))
    return ''.join(decrypted_msg)

msg1 = encrypt_square_code("have a nice day")
msg2 = encrypt_square_code("feed the dog")
msg3 = encrypt_square_code("chill out")
msg4 = encrypt_square_code("if man was meant to stay on the ground god would have given us roots")
decrypt_square_code(msg1)
decrypt_square_code(msg2)
decrypt_square_code(msg3)
decrypt_square_code(msg4)