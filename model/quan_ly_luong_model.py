import pandas as pd

class QuanLyLuongModel:
    def __init__(self, filename: str):
        self.filename = filename
        self.columns = ["Mã NV", "Họ Tên", "Chức vụ", "Lương cơ bản", "Thưởng", "Phạt", "Giờ làm thêm", "Lương thực nhận"]
        self.df = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.filename)
            for col in self.columns:
                if col not in df.columns:
                    df[col] = None
            return df[self.columns]
        except FileNotFoundError:
            return pd.DataFrame(columns=self.columns)

    def get_dataframe(self) -> pd.DataFrame:
        return self.df

    def get_all(self) -> pd.DataFrame:
        return self.get_dataframe()

    def add_employee(self, data: dict):
        new_row = pd.DataFrame([data])
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self._save()

    def _save(self):
        self.df.to_csv(self.filename, index=False)
