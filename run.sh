python run_classifier.py \
--task_name=emlo \
--do_train=true \
--do_eval=true \
--data_dir=./glue \
--vocab_file=./uncased/uncased_L-12_H-768_A-12/vocab.txt \
--bert_config_file=./uncased/uncased_L-12_H-768_A-12/bert_config.json \
--init_checkpoint=./uncased/uncased_L-12_H-768_A-12/bert_model.ckpt \
--max_seq_length=200 \
--train_batch_size=16 \
--learning_rate=2e-5 \
--num_train_epochs=6.0 \
--output_dir=./tmp/emotion/

