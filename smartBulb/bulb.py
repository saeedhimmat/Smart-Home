from re import search
from time import sleep
from yeelight import Bulb


class My_bulb(Bulb):
    def __init__(self, ip="0", unit_time=0.3):
        super().__init__(ip)
        self.ip = ip
        self.unit_time = unit_time

    def get_ip(self):
        print(f'{self.ip}')

    def dot(self):
        print("• ", end='')
        self.turn_on(effect="smooth", duration=0)
        sleep(self.unit_time)
        self.turn_off(effect="smooth", duration=0)
        sleep(self.unit_time)

    def dash(self):
        print("_ ", end='')
        self.turn_on(effect="smooth", duration=0)
        sleep(self.unit_time * 3)
        self.turn_off(effect="smooth", duration=0)
        sleep(self.unit_time)

    def morse_space(self):
        sleep(self.unit_time * 7)

    def morse_letter_a(self):
        self.dot()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_b(self):
        self.dash()
        self.dot()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_c(self):
        self.dash()
        self.dot()
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_d(self):
        self.dash()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_e(self):
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_f(self):
        self.dot()
        self.dot()
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_g(self):
        self.dash()
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_h(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_i(self):
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_j(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_k(self):
        self.dash()
        self.dot()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_l(self):
        self.dot()
        self.dash()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_m(self):
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_n(self):
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_o(self):
        self.dash()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_p(self):
        self.dot()
        self.dash()
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_q(self):
        self.dash()
        self.dash()
        self.dot()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_r(self):
        self.dot()
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_s(self):
        self.dot()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_letter_t(self):
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_u(self):
        self.dot()
        self.dot()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_v(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash()
        self.turn_off(effect="smooth", duration=0)

    def morse_letter_w(self):
        self.dot()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_x(self):
        self.dash()
        self.dot()
        self.dot()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_y(self):
        self.dash()
        self.dot()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_letter_z(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_number_1(self):
        self.dot()
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_number_2(self):
        self.dot()
        self.dot()
        self.dash()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_number_3(self):
        self.dot()
        self.dot()
        self.dot()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_number_4(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_number_5(self):
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_number_6(self):
        self.dash()
        self.dot()
        self.dot()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_number_7(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_number_8(self):
        self.dash()
        self.dash()
        self.dash()
        self.dot()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_number_9(self):
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        self.dot()
        sleep(self.unit_time * 3)

    def morse_number_0(self):
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        self.dash()
        sleep(self.unit_time * 3)

    def morse_code(self, massage: str):
        switcher = {
            32: self.morse_space,
            48: self.morse_number_0,
            49: self.morse_number_1,
            50: self.morse_number_2,
            51: self.morse_number_3,
            52: self.morse_number_4,
            53: self.morse_number_5,
            54: self.morse_number_6,
            55: self.morse_number_7,
            56: self.morse_number_8,
            57: self.morse_number_9,
            97: self.morse_letter_a,
            98: self.morse_letter_b,
            99: self.morse_letter_c,
            100: self.morse_letter_d,
            101: self.morse_letter_e,
            102: self.morse_letter_f,
            103: self.morse_letter_g,
            104: self.morse_letter_h,
            105: self.morse_letter_i,
            106: self.morse_letter_j,
            107: self.morse_letter_k,
            108: self.morse_letter_l,
            109: self.morse_letter_m,
            110: self.morse_letter_n,
            111: self.morse_letter_o,
            112: self.morse_letter_p,
            113: self.morse_letter_q,
            114: self.morse_letter_r,
            115: self.morse_letter_s,
            116: self.morse_letter_t,
            117: self.morse_letter_u,
            118: self.morse_letter_v,
            119: self.morse_letter_w,
            120: self.morse_letter_x,
            121: self.morse_letter_y,
            122: self.morse_letter_z,
        }
        if search("[^a-zA-Z0-9 ]", massage):
            print("\nPlease enter only letters and numbers")

        else:
            for letter in massage:
                print("\nsending: " + letter + "        ", end="")
                letter = letter.lower()
                letter = ord(letter)
                try:
                    mc = switcher.get(letter)
                    mc()
                except:
                    print("Device is not available")
