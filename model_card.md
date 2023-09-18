# Model Card


## Model Details

The model yielded by this project is a scikit-learn Random Forest Classifier trained on the Census dataset.

## Intended Use

The model should be used to predict salary of people based on different attributes (numertical and categorical).

## Training Data

The original datan is splitted into two chuncks (80% train, 20 % test)

## Evaluation Data

The original data is splitted into two chuncks (20% test)

## Metrics
To mesure the performance of our model, we used 3 different metrics:

    - Precision
    - Recall
    - Fbeta  


On the train set the model yielded the following values:
- Precision: 88.69 %
- Recall: 72.31 %
- Fbeta: 79.60 %

Using the evaluation data, our model gave the following results:
- Precision: 89.35 %
- Recall: 72.07 %
- Fbeta: 79.79 %

A more detailed results are provided in the `model/slice_output.txt` file. 
## Ethical Considerations

Given the slice study performed on the categorical features, 
We found that the performance on the race feature vary slightly between different ethnicities.
A study on the faireness and unbiasedness of the model is highly recommended before use.


## Caveats and Recommendations
Given the different categories, we recommend a dedicated study to understand the impact of variation on the final results.
