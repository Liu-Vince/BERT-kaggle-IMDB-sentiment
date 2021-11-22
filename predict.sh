python run_classifier.py \
  --task_name=emlo \
  --do_predict=true \
  --data_dir=./glue \
  --vocab_file=./uncased/uncased_L-12_H-768_A-12/vocab.txt \
  --bert_config_file=./uncased/uncased_L-12_H-768_A-12/bert_config.json \
  --init_checkpoint=./tmp/emotion/ \
  --max_seq_length=200 \
  --output_dir=./tmp/emotion_out/
