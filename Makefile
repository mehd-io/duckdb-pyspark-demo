IMAGE_NAME=local/duckspark
SCRIPT=duckspark.py

.PHONY: build data duckspark pyspark

build:
	@if [ -z $$(docker images -q $(IMAGE_NAME)) ]; then \
		echo "Building Docker image $(IMAGE_NAME)..."; \
		docker build -t $(IMAGE_NAME) .; \
	else \
		echo "Docker image $(IMAGE_NAME) already exists."; \
	fi

data:
	mkdir -p data
	curl https://us-prd-motherduck-open-datasets.s3.amazonaws.com/hacker_news/parquet/hacker_news_2021_2022.parquet -o data/hacker_news_2021_2022.parquet

duckspark: build
	docker run -it --rm -v "$(PWD)":/app -v $(PWD)/data:/data $(IMAGE_NAME) /bin/bash -c "time python /app/$(SCRIPT)"

pyspark:
	docker run -it -v $(PWD)/$(SCRIPT):/app/$(SCRIPT) -v $(PWD)/data:/data apache/spark-py:v3.4.0 \
    /bin/bash -c "time /opt/spark/bin/spark-submit --conf spark.executor.memory=10g --conf spark.driver.memory=12g /app/$(SCRIPT)"






