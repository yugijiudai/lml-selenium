# Author : lml
# Date : 2021/12/22


class ClassGeneratorUtil:

    @staticmethod
    def generate_cls(clz, filepath, params=None) -> None:
        """
        自动生成类和getter setter
        :param clz: 类名字符串
        :param filepath: 路径字符串，最好绝对路径，如果生成在当前目录就写空字符串
        :param params: 类中的属性列表
        """
        if params is None:
            params = []

        lines = [
            f"class {clz}:"
        ]

        lines += ['\t__slots__ = ' + str(tuple([f"__{param}" for param in params])) + "\n"]
        lines += ["\tdef __init__(self):"]
        lines += [f"\t\tself.__{param} = None" for param in params]
        lines += [""]
        for param in params:
            lines += [
                "\t@property",
                f"\tdef {param}(self):",
                f"\t\treturn self.__{param}\n",
                f"\t@{param}.setter",
                f"\tdef {param}(self, value):",
                f"\t\tself.__{param} = value\n"
            ]
        lines.append("\tdef to_dict(self):")
        lines.append('\t\treturn {')
        lines += [f'\t\t\t"{param}": self.__{param},' for param in params]
        lines.append('\t\t}')
        lines = [i + "\n" for i in lines]
        with open(filepath, "w+", encoding="utf-8") as fp:
            fp.writelines(lines)
            print(f"类{clz}生成成功,路径{filepath}")
