####
###Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
###Your task is to write a function maskify, which changes all but the last four characters into '#'.
###

cc = "poopoopeepeexdddddd"
cc_list = list(cc)

print(cc_list)
print(len(cc_list))

if len(cc_list) > 4:
    print('longer than 4')
    for i in range(len(cc_list)):
        cc_list[i] = '#'
        if len(cc_list) - i == 5:
            break

print(cc_list)
cc = ''.join(cc_list)
print(cc)