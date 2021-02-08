def run_length_encode_2d(img_array):
    encoded_img_array = []
    counter_num = 1

    num_ref = img_array[0][0]
    img_array[0].pop(0)

    for lista in img_array:
        for numero in lista:

            if numero == num_ref:
                counter_num += 1
            
            else:
                encoded_img_array.append((counter_num, num_ref))
                counter_num = 1

            
            num_ref = numero

    encoded_img_array.append((counter_num, num_ref))

    return encoded_img_array
            
