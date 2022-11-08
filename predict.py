import pandas

def predict(model, X):
    y = model.predict(X.astype('float32')/255)
    y = y.argmax()
    return y
