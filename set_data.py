import struct
import sys
import binascii

file_list = {
    "q1p0k0_kernel_UMA_2097152_region0_0x00007fede2000000.dat",
    "q1p0k0_kernel_UMA_2097152_region0_0x00007feefb600000.dat",
    "q1p0k0_kernel_UMA_2097152_region0_0x00007feefb6b4000.dat",
    "q1p0k0_kernel_UMA_2097152_region0_0x00007feeffe00000.dat",
    "q1p0k0_kernel_UMA_2097152_region0_0x00007feeffeb4000.dat"
}


def set_value():
    hex_value = "803f"  # bf16 1.0
    bit_width = len(hex_value)
    # hex string to string(char)
    fill_value = []
    for i in range(0, bit_width, 2):
        # fill_value.join(chr(int(hex_value[i:i + 2], 16)))
        # print(binascii.unhexlify(hex_value[i:i + 2]))
        # fill_value.join(binascii.unhexlify(hex_value[i:i + 2]))
        fill_value.append(struct.pack("B", (int(hex_value[i:i + 2], 16))))
    # fill_value = [].extend(
    #     struct.pack("B", (int(hex_value[i:i + 2], 16)))
    #     for i in range(0, bit_width, 2))
    print(fill_value)
    # print(int(hex_value[:2], 16), int(hex_value[2:4], 16), fill_value)

    for i in file_list:
        # fill_data = ""
        with open(i, "rb") as f:
            file_length = len(f.read())
            print("length is 0x{:08X}".format(file_length))
            # for _ in range(0, file_length, bit_width):
            #     fill_data += fill_value
        # print(fill_data)
        with open(i, "wb") as f:
            for _ in range(0, file_length, bit_width // 2):
                for j in fill_value:
                    f.write(j)


if __name__ == '__main__':
    set_value()