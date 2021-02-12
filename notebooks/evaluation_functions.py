from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report, plot_confusion_matrix
import matplotlib.pyplot as plt

def pr_curves(y_test_multi, y_hat_test_multi, classes):
    """
    Display the Precision Recall Curves for Multi Class Data.
    """
    # Compute PR curve and PR area for each class
    precision = dict()
    recall = dict()
    pr_auc = dict()
    for i in range(3):
        precision[i], recall[i], _ = precision_recall_curve(y_test_multi[:, i], y_hat_test_multi[:, i])
        pr_auc[i] = auc(recall[i], precision[i])

    # Plot of a PR curve for a specific class
    for i, class_ in enumerate(classes):
        plt.figure()
        plt.plot(recall[i], precision[i], label='PR curve (area = %0.2f)' % pr_auc[i])
        plt.plot([0, 1], [1, 0], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title(f'Precision Recall Curve for {class_.title()}')
        plt.legend(loc="lower left")
        plt.show()

def roc_curves(y_test_multi, y_hat_test_multi, classes):
    """
    Display the ROC Curves for Multi Class Data
    """
    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(3):
        fpr[i], tpr[i], _ = roc_curve(y_test_multi[:, i], y_hat_test_multi[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Plot of a ROC curve for a specific class
    for i, class_ in enumerate(classes):
        plt.figure()
        plt.plot(fpr[i], tpr[i], label='ROC curve (area = %0.2f)' % roc_auc[i])
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'Receiver operating characteristic for {class_.title()}')
        plt.legend(loc="lower right")
        plt.show()

def confustion_matrix_and_classification_report(estimator, X, y, labels, set_name):
    """
    Display a Classfication Report and Confusion Matrix for the given data.
    """

    predictions = estimator.predict(X)

    print(f'Classification Report for {set_name} Set')
    print(classification_report(y, predictions, target_names=labels))

    matrix = plot_confusion_matrix(estimator,
                                   X,
                                   y,
                                   display_labels = labels,
                                   cmap = plt.cm.Blues,
                                   xticks_rotation = 70,
                                   values_format = 'd')
    matrix.ax_.set_title(f'{set_name} Set Confustion Matrix, without Normalization')

    plt.show()

    matrix = plot_confusion_matrix(estimator,
                                   X,
                                   y,
                                   display_labels = labels,
                                   cmap = plt.cm.Blues,
                                   xticks_rotation = 70,
                                   normalize = 'true')
    matrix.ax_.set_title(f'{set_name} Set Confustion Matrix, with Normalization')

    plt.show()
