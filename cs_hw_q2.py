import datetime
def hamming_encode(data):
    m = len(data)
    k = 0
    while 2 ** k < m + k + 1:
        k += 1

    encoded_message = [None] * (m + k)

    j = 0
    data_index = 0
    for i in range(1, m + k + 1):
        if i == 2 ** j:
            encoded_message[i - 1] = 0
            j += 1
        else:
            encoded_message[i - 1] = int(data[data_index])
            data_index += 1

    for j in range(k):
        parity_position = 2 ** j
        parity_value = 0
        for i in range(1, m + k + 1):
            if (i >> j) & 1:
                parity_value ^= encoded_message[i - 1]
        encoded_message[parity_position - 1] = parity_value

    return ''.join(map(str, encoded_message))
def hamming_decode(data, k):
    m = len(data) - k
    decoded_message = list(data)

    error_position = 0
    for j in range(k):
        parity_position = 2 ** j
        parity_value = 0
        for i in range(1, m + k + 1):
            if (i >> j) & 1:
                parity_value ^= int(decoded_message[i - 1])
        if parity_value != int(decoded_message[parity_position - 1]):
            error_position += parity_position

    if error_position == 0:
        return "No error"
    else:
        decoded_message[error_position - 1] = str(1 - int(decoded_message[error_position - 1]))
        corrected_data = ''.join(decoded_message[:m])
        return f"Error at Position {error_position}, and correct data: {corrected_data}"


# Example usage:
org_sig1 = '1101'
encoded_sig1 = hamming_encode(org_sig1)
print(f"Original Data: {org_sig1}")
print(f"Encoded Data: {encoded_sig1}")
decoded_sig1 = hamming_decode(encoded_sig1, 3)
print(f"Decoded Data: {decoded_sig1}")

# Additional Example:
org_sig2 = '0011101'
encoded_sig2 = hamming_encode(org_sig2)
decoded_sig2 = hamming_decode(encoded_sig2, 4)
print("Original Data:", org_sig2)
print("Encoded Data:", encoded_sig2)
print("Decoded Data:", decoded_sig2)
print()
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")