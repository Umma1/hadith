from hadith import (Musnad_Ahmed, Muwatta_Malik, Sahih_Bukhari, Sahih_Muslim,
                    Sunan_Abu_Dawud, Sunan_Al_Darami, Sunan_Al_Nasai,
                    Sunan_Al_Tirmidhi, Sunan_Ibn_Maja)


def test_musnad_ahmed():
    sb = Musnad_Ahmed()
    assert sb.get_hadiths().shape[0] == 18444


def test_muwatta_malik():
    sb = Muwatta_Malik()
    assert sb.get_hadiths().shape[0] == 1594


def test_sahih_bukhari():
    sb = Sahih_Bukhari()
    assert sb.get_hadiths().shape[0] == 7008


def test_sahih_muslim():
    sb = Sahih_Muslim()
    assert sb.get_hadiths().shape[0] == 5362


def test_sunan_abu_dawud():
    sb = Sunan_Abu_Dawud()
    assert sb.get_hadiths().shape[0] == 4600


def test_sunan_al_darami():
    sb = Sunan_Al_Darami()
    assert sb.get_hadiths().shape[0] == 3367


def test_sunan_al_nasai():
    sb = Sunan_Al_Nasai()
    assert sb.get_hadiths().shape[0] == 5662


def test_sunan_al_tirmidhi():
    sb = Sunan_Al_Tirmidhi()
    assert sb.get_hadiths().shape[0] == 3891


def test_sunan_ibn_maja():
    sb = Sunan_Ibn_Maja()
    assert sb.get_hadiths().shape[0] == 4350
