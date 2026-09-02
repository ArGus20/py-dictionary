from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.dictionary = [()] * 8
        self.count = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % len(self.dictionary)

        if self.count >= len(self.dictionary) * (2 / 3):
            old_dict = self.dictionary.copy()
            self.dictionary = [()] * len(self.dictionary) * 2
            self.count = 0

            index = hash(key) % len(self.dictionary)

            for element in old_dict:
                if element:
                    self[element[0]] = element[2]

        if self.dictionary[index] and self.dictionary[index][0] != key:
            for _ in range(len(self.dictionary)):
                if not self.dictionary[index]:
                    self.count += 1
                    break
                if self.dictionary[index] and self.dictionary[index][0] == key:
                    self.dictionary[index] = (key, hash(key), value)
                    break
                if index == len(self.dictionary) - 1:
                    index = 0
                else:
                    index += 1

            self.dictionary[index] = (key, hash(key), value)
        else:
            if not self.dictionary[index]:
                self.count += 1
            self.dictionary[index] = (key, hash(key), value)

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % len(self.dictionary)
        if self.dictionary[index] and self.dictionary[index][0] == key:
            return self.dictionary[index][2]
        if self.dictionary[index] and self.dictionary[index][0] != key:
            for _ in range(len(self.dictionary)):
                if index == len(self.dictionary) - 1:
                    index = 0
                else:
                    index += 1
                if self.dictionary[index] and self.dictionary[index][0] == key:
                    return self.dictionary[index][2]

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.count
