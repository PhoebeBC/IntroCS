class Caesar:

    def __init__(self, file_handle_plain, file_handle_secret, file_handle_result):
        self.file_handle = file_handle_plain
        self.file_handle_secret = file_handle_secret
        self.file_handle_result = file_handle_result

    def encode_to_file(self, rotations) :
        for line in self.file_handle:
            cipher_line = self.caesar_cipher(line, rotations)
            rotations += len(line)
            self.write_to_file_secret(cipher_line)

    def decode_to_file(self, rotations):
        for line in self.file_handle_secret:
            cipher_line = self.caesar_cipher(line, (rotations * -1))
            rotations += len(line)
            self.write_to_file_result(cipher_line, self.file_handle_result)

    def write_to_file_secret(self, ciphered):
        self.file_handle_secret.write(ciphered)

    def write_to_file_result(self, ciphered, result_handle):
        result_handle.write(ciphered)

    def caesar_cipher(self, word, rotations):
        cipher_word = ""
        for character in word:
            cipher_chapracter = chr((ord(character) + int(rotations)) % 127)
            cipher_word += cipher_character
            if rotations < 0:
                rotations -= 1
            else:
                rotations += 1

        return cipher_word
