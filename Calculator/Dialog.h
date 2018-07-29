#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>

namespace Ui {
class Dialog;
}

class Dialog : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = 0);
    ~Dialog();

private slots:


    void on_num1_clicked();

    void on_num2_clicked();

    void on_num3_clicked();

    void on_num4_clicked();

    void on_num5_clicked();

    void on_num6_clicked();

    void on_num7_clicked();

    void on_num8_clicked();

    void on_num9_clicked();

    void on_num0_clicked();

    void on_Backspace_clicked();

    void on_sign_clicked();

    void on_CE_clicked();

    void on_C_clicked();

    void on_equal_clicked();

    void on_add_clicked();

    void on_sub_clicked();

    void on_multiply_clicked();

    void on_divide_clicked();

    void on_spot_clicked();

    void on_reciprocal_clicked();

    void on_square_clicked();

    void on_sqrt_clicked();

private:
    Ui::Dialog *ui;
};

#endif // DIALOG_H
