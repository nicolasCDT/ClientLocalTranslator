to_translate_dict = {}
translate_base_dict = {}
success_lines = []
errors_lines = []

print("Metin2 translate project : client version 1.0")

print("Loading to_translate.txt...")
with open("to_translate.txt", "r") as file:
    for line in file.readlines():
        line = line.split("\t")
        if len(line) != 1:
            to_translate_dict[line[0]] = "\t".join(line[1:])

print("Loading translate_base.txt...")
with open("translate_base.txt", "r") as file:
    for line in file.readlines():
        line = line.split("\t")
        if len(line) != 1:
            translate_base_dict[line[0]] = "\t".join(line[1:])

with open("result.txt", "w") as result_file:
    with open("other.txt", "w") as other_files:
        to_translate_set = set(to_translate_dict)
        translate_base_set = set(translate_base_dict)

        inter = to_translate_set.intersection(translate_base_set)

        print("Making...")
        for key in sorted(to_translate_dict):
            if key in inter:
                success_lines.append("{0}\t{1}\n".format(key, translate_base_dict[key].replace("\n", "")))
            else:
                errors_lines.append("{0}\t{1}\n".format(key, to_translate_dict[key].replace("\n", "")))

        other_files.writelines(errors_lines)
        result_file.writelines(success_lines)
print("Done.")
