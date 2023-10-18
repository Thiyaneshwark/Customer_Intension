from django.shortcuts import render
import pandas as pd
import joblib

def predict(request):
    if request.method == 'POST':
        input_data = {
            'ProductRelated': int(request.POST['ProductRelated']),
            'ProductRelated_Duration': float(request.POST['ProductRelated_Duration']),
            'ExitRates': float(request.POST['ExitRates']),
            'PageValues': float(request.POST['PageValues']),
            'Month': int(request.POST['Month']),

        }

        input_df = pd.DataFrame([input_data])
        
        # Load the pre-trained model
        model = joblib.load('E:\customerIntension\savedModels\custIn.joblib')
        
        # Make predictions using the model
        prediction = model.predict(input_df)
        
        # Assuming your model predicts binary outcomes (0 or 1)
        result = "NO_purhcase_made" if prediction[0] == 1 else "Purchase_made"

        return render(request, 'result.html', {'result': result})

    return render(request, 'index.html')
