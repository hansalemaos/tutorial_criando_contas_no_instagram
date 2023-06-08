from random import uniform, choice
from string import ascii_letters
from time import sleep
from gettmpmail import get_tmp_email
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium2df_locate_element import selenium2dfwait, locate_element


def usleep(a, b):
    sleep(uniform(a, b))


if __name__ == "__main__":
    chrome_opt = uc.ChromeOptions()
    chrome_opt.add_argument("--incognito")
    driver = uc.Chrome(
        options=chrome_opt,
    )
    selenium2dfwait.driver = driver
    driver.get(r"https://instagram.com")
    df2 = get_tmp_email(n=1, timeout=30, imapfile=None)
    q = df2.aa_checkmail.iloc[0]()
    #####################################################################################################
    # if __name__ !='__main__':
    _, df = locate_element(
        checkdf=lambda df: df.loc[
            df.aa_innerText.str.contains("Decline", na=False)
            & (df.aa_localName == "button")
        ]
    )
    df.se_click.iloc[0]()
    usleep(3, 5)
    #####################################################################################################

    _, df = locate_element(
        checkdf=lambda df: df.loc[
            df.aa_innerHTML.str.contains(r"\b[sS]ign up\b$", regex=True, na=False)
        ]
    )
    df.se_click.iloc[0]()
    usleep(3, 5)
    #####################################################################################################

    _, df = locate_element(
        checkdf=lambda df: df.loc[df.aa_localName.str.contains("input")]
    )
    df.iloc[0].se_send_keys(df2.aa_email.iloc[0])
    usleep(0.05, 0.11)
    df.iloc[1].se_send_keys(df2.aa_fullname.iloc[0])
    usleep(0.05, 0.11)
    instausername = df2.aa_fullname.iloc[0].replace(" ", choice(ascii_letters)).strip()
    df.iloc[2].se_send_keys(instausername)
    usleep(0.05, 0.11)
    df.iloc[3].se_send_keys(df2.aa_password.iloc[0])
    usleep(1, 2)
    #####################################################################################################
    _, df = locate_element(
        checkdf=lambda df: df.loc[
            (df.aa_innerText == "Next") & (df.aa_localName == "button")
        ]
    )
    df.iloc[0].se_click()
    usleep(3, 5)
    #####################################################################################################
    _, df = locate_element(checkdf=lambda df: df.loc[df.aa_localName == "select"])
    lili = list(range(20))
    lili = lili[1:]
    for xa in range(choice(lili[:2])):
        df.se_send_keys.iloc[0](Keys.PAGE_DOWN)
        usleep(0.05, 0.11)

    for xa in range(choice(lili[:3])):
        df.se_send_keys.iloc[1](Keys.PAGE_DOWN)
        usleep(0.05, 0.11)

    for xa in range(choice(lili[9:])):
        df.se_send_keys.iloc[2](Keys.PAGE_DOWN)
        usleep(0.05, 0.11)
    #####################################################################################################
    _, df = locate_element(
        checkdf=lambda df: df.loc[
            (df.aa_innerText == "Next") & (df.aa_localName == "button")
        ]
    )
    df.iloc[0].se_click()
    sleep(uniform(6, 8))
    #####################################################################################################
    code = ""
    while True:
        try:
            fa = df2.aa_checkmail.iloc[0]()
            code = fa["hydra:member"][0]["subject"][:6]
            int(code)
            break
        except Exception as fa:
            print(fa)
            sleep(5)
            continue
    #####################################################################################################
    _, df = locate_element(
        checkdf=lambda df: df.loc[df.aa_localName.str.contains("input")]
    )
    df.iloc[0].se_send_keys(code)
