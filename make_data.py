import pdb
import json


def make_data(src_path, tgt_path):
    def create_content(data_item, label_needed):
        human_qa = data_item["prefix"] + " " + data_item["answer"]
        machine_qa = data_item["output_without_watermark"]
        return [human_qa, machine_qa][label_needed]
    
    with open(src_path, 'r') as fin, open(tgt_path, 'w') as fout:
        for line in fin:
            data_item = json.loads(line)
            for label in [0, 1]:
                new_data_item = {"content": create_content(data_item, label), "label": label}            
                new_data_item_str = json.dumps(new_data_item)
                fout.write(new_data_item_str)
                fout.write("\n")


if __name__ == '__main__':
    src_path = "/root/zhenting/probing/data/lfqa_umd.jsonl"
    tgt_path = "/root/zhenting/probing/data/lfqa_umd_transformed.jsonl"
    make_data(src_path, tgt_path)