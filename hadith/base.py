import os

import pandas as pd


class MuhadithMixin:
    """Mixin for Muhadithins (محدّثين)
    مجموعة دوّال  ستستخدم في لكل المحدّثين
    """
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self._data_loaded = False

    def _load_data(self, file_name):
        return pd.read_csv(file_name, encoding='utf8')

    def get_hadiths(self, with_tashkil=True):
        """Returns all hadiths for Muhadith"""
        file_path = os.path.join(self.base_path, "data")
        file_path = os.path.join(file_path, self.filename_with_tashkil)

        if not os.path.exists(file_path):
            raise IOError("The data file for Muhadith is missing"
                          f" from path: {file_path}")

        if not self._data_loaded:
            self._data = self._load_data(file_path)
            self._data_loaded = True

        return self._data


class Sahih_Bukhari(MuhadithMixin):
    """Loads and handles hadiths reported by Sahih Bukhari
    صحيح البخاري
    """
    def __init__(self):
        super(Sahih_Bukhari, self).__init__()
        self.filename_with_tashkil = "Sahih_Bukhari.csv.gz"


class Sahih_Muslim(MuhadithMixin):
    """Loads and handles hadiths reported by Sahih Muslim
    صحيح مسلم
    """
    def __init__(self):
        super(Sahih_Muslim, self).__init__()
        self.filename_with_tashkil = "Sahih_Muslim.csv.gz"


class Muwatta_Malik(MuhadithMixin):
    """Loads and handles hadiths reported by Muwatta Malik
    موطأ الإمام مالك
    """
    def __init__(self):
        super(Muwatta_Malik, self).__init__()
        self.filename_with_tashkil = "Maliks_Muwatta.csv.gz"


class Musnad_Ahmed(MuhadithMixin):
    """Loads and handles hadiths reported by Musnad Ahmed
    مسند الإمام أحمد
    """
    def __init__(self):
        super(Musnad_Ahmed, self).__init__()
        self.filename_with_tashkil = "Musnad_Ahmad_ibn_Hanbal.csv.gz"


class Sunan_Abu_Dawud(MuhadithMixin):
    """Loads and handles hadiths reported by Sunan Abu Dawud
    سنن أبو داود
    """
    def __init__(self):
        super(Sunan_Abu_Dawud, self).__init__()
        self.filename_with_tashkil = "Sunan_Abu_Dawud.csv.gz"


class Sunan_Al_Darami(MuhadithMixin):
    """Loads and handles hadiths reported by Sunan Al Darami
    سنن الدّرامي
    """
    def __init__(self):
        super(Sunan_Al_Darami, self).__init__()
        self.filename_with_tashkil = "Sunan_al_Darami.csv.gz"


class Sunan_Al_Tirmidhi(MuhadithMixin):
    """Loads and handles hadiths reported by Sunan Al Tirmidthi
    سنن الترميذي
    """
    def __init__(self):
        super(Sunan_Al_Tirmidhi, self).__init__()
        self.filename_with_tashkil = "Sunan_al_Tirmidhi.csv.gz"


class Sunan_Al_Nasai(MuhadithMixin):
    """Loads and handles hadiths reported by Sunan Al Nasai
    سنن النسائي
    """
    def __init__(self):
        super(Sunan_Al_Nasai, self).__init__()
        self.filename_with_tashkil = "Sunan_al-Nasai.csv.gz"


class Sunan_Ibn_Maja(MuhadithMixin):
    """Loads and handles hadiths reported by Sunan Ibn Maja
    سنن إبن ماجة
    """
    def __init__(self):
        super(Sunan_Ibn_Maja, self).__init__()
        self.filename_with_tashkil = "Sunan_Ibn_Maja.csv.gz"
