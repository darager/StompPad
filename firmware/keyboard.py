import usb_hid

class Keyboard:
    def __init__(self):
        self._report = bytearray(8)

    def _send(self) -> None:
        usb_hid.report(usb_hid.KEYBOARD, self._report)

    def _modifier(self, keycode : int) -> int:
        if keycode >= Key.MOD_LEFT_CTRL and keycode <= Key.MOD_RIGHT_GUI:
            return 1 << (keycode - Key.MOD_LEFT_CTRL)

    def _add_to_report(self, keycode : int) -> None:
        modifier_bit = self._modifier(keycode)
        if modifier_bit:
            self._report[0] |= modifier_bit
        else:
            done = False
            for i in range(6):
                if self._report[2+i] == keycode:
                    done = True
                    break
            if not done:
                for i in range(6):
                    if self._report[2+i] == 0:
                        self._report[2+i] = keycode
                        done = True
                        break
                if not done:
                    raise ValueError("more than 6 keys")

    def _remove_from_report(self, keycode : int) -> None:
        modifier_bit = self._modifier(keycode)
        if modifier_bit:
            self._report[0] &= ~modifier_bit
        else:
            for i in range(6):
                if self._report[2+i] == keycode:
                    self._report[2+i] = 0
                    break

    def press(self, *keycodes : int) -> None:
        for k in keycodes:
            self._add_to_report(k)
        self._send()

    def release(self, *keycodes : int) -> None:
        for k in keycodes:
            self._remove_from_report(k)
        self._send()

    def release_all(self) -> None:
        for i in range(8):
            self._report[i] = 0
        self._send()

class Key:
    # https://deskthority.net/wiki/Scancode
    MOD_LEFT_CTRL   = 0xe0
    MOD_LEFT_SHIFT  = 0xe1
    MOD_LEFT_ALT    = 0xe2
    MOD_LEFT_GUI    = 0xe3
    MOD_RIGHT_CTRL  = 0xe4
    MOD_RIGHT_SHIFT = 0xe5
    MOD_RIGHT_ALT   = 0xe6
    MOD_RIGHT_GUI   = 0xe7

    CODE_A  = 0x04 # a-z 0x04-0x1d
    CODE_0  = 0x27
    CODE_1  = 0x1e # 1-9 0x1e-0x26
    CODE_F1 = 0x3a # f1-f12 0x3a-0x45

    a = 0x04
    b = 0x05
    c = 0x06
    ç = 0x37
    d = 0x07
    e = 0x08
    f = 0x09
    g = 0x0a
    ğ = 0x2f
    h = 0x0b
    i = 0x0c
    j = 0x0d
    k = 0x0e
    l = 0x0f
    m = 0x10
    n = 0x11
    o = 0x12
    ö = 0x36
    p = 0x13
    q = 0x14
    r = 0x15
    s = 0x16
    ş = 0x33
    t = 0x17
    u = 0x18
    ü = 0x30
    v = 0x19
    w = 0x1a
    x = 0x1b
    y = 0x1c
    z = 0x1d

    A = [MOD_LEFT_SHIFT, 0x04]
    B = [MOD_LEFT_SHIFT, 0x05]
    C = [MOD_LEFT_SHIFT, 0x06]
    Ç = [MOD_LEFT_SHIFT, 0x37]
    D = [MOD_LEFT_SHIFT, 0x07]
    E = [MOD_LEFT_SHIFT, 0x08]
    F = [MOD_LEFT_SHIFT, 0x09]
    G = [MOD_LEFT_SHIFT, 0x0a]
    Ğ = [MOD_LEFT_SHIFT, 0x2f]
    H = [MOD_LEFT_SHIFT, 0x0b]
    I = [MOD_LEFT_SHIFT, 0x0c]
    İ = [MOD_LEFT_SHIFT, 0x34]
    J = [MOD_LEFT_SHIFT, 0x0d]
    K = [MOD_LEFT_SHIFT, 0x0e]
    L = [MOD_LEFT_SHIFT, 0x0f]
    M = [MOD_LEFT_SHIFT, 0x10]
    N = [MOD_LEFT_SHIFT, 0x11]
    O = [MOD_LEFT_SHIFT, 0x12]
    Ö = [MOD_LEFT_SHIFT, 0x36]
    P = [MOD_LEFT_SHIFT, 0x13]
    Q = [MOD_LEFT_SHIFT, 0x14]
    R = [MOD_LEFT_SHIFT, 0x15]
    S = [MOD_LEFT_SHIFT, 0x16]
    Ş = [MOD_LEFT_SHIFT, 0x33]
    T = [MOD_LEFT_SHIFT, 0x17]
    U = [MOD_LEFT_SHIFT, 0x18]
    Ü = [MOD_LEFT_SHIFT, 0x30]
    V = [MOD_LEFT_SHIFT, 0x19]
    W = [MOD_LEFT_SHIFT, 0x1a]
    X = [MOD_LEFT_SHIFT, 0x1b]
    Y = [MOD_LEFT_SHIFT, 0x1c]
    Z = [MOD_LEFT_SHIFT, 0x1d]

    Num_0 = 0x27
    Num_1 = 0x1e
    Num_2 = 0x1f
    Num_3 = 0x20
    Num_4 = 0x21
    Num_5 = 0x22
    Num_6 = 0x23
    Num_7 = 0x24
    Num_8 = 0x25
    Num_9 = 0x26