#include "dialog.h"
#include "ui_dialog.h"
#include "math.h"

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
    setWindowTitle("Calculate");
    ui->display->setText("0");
}

Dialog::~Dialog()
{
    delete ui;
}

bool isResult=false;
bool Lock=false;
bool hasCalculate=false;
QString a="0";
QString Result="0";
int op=-1;

void Dialog::on_num1_clicked()
{
    if(Lock)
        Lock=false;
    QString S="1";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num2_clicked()
{
    if(Lock)
        Lock=false;
    QString S="2";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num3_clicked()
{
    if(Lock)
        Lock=false;
    QString S="3";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num4_clicked()
{
    if(Lock)
        Lock=false;
    QString S="4";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num5_clicked()
{
    if(Lock)
        Lock=false;
    QString S="5";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num6_clicked()
{
    if(Lock)
        Lock=false;
    QString S="6";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num7_clicked()
{
    if(Lock)
        Lock=false;
    QString S="7";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num8_clicked()
{
    if(Lock)
        Lock=false;
    QString S="8";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num9_clicked()
{
    if(Lock)
        Lock=false;
    QString S="9";
    if(a!="0")
        a+=S;
    else
        a=S;
    ui->display->setText(a);
    hasCalculate=false;
}

void Dialog::on_num0_clicked()
{
    if(Lock)
        Lock=false;
    QString S="0";
    if(ui->display->text()!="0")
    {
        if(a!="0")
        {
            a+=S;
            ui->display->setText(a);
        }
        else
        {
            ui->display->setText(a);
        }
    }
    hasCalculate=false;
}

void Dialog::on_Backspace_clicked()
{
    if(!Lock)
    {
        QString S=ui->display->text();
        a=S.left(S.length()-1);
        if(a==""||a=="-")
            a="0";
        ui->display->setText(a);
    }
}

void Dialog::on_sign_clicked()
{
    QString S="-";
    if(a!="0")
    {
        if(a.left(1)=="-")
            a.replace(QString("-"), QString(""));
        else
        {
            a=S+a;
        }
        ui->display->setText(a);
    }
}

void Dialog::on_CE_clicked()
{
    a="0";
    ui->display->setText(a);
    if(Lock)
        Dialog::on_C_clicked();

}

void Dialog::on_C_clicked()
{
    a="0";
    Result="0";
    Lock=false;
    isResult=false;
    hasCalculate=false;
    op=-1;
    ui->display->setText(a);
}

void Dialog::on_equal_clicked()
{
    if(op!=-1)
    {
        if(op==1)
        {
            double d1=Result.toDouble();
            double d2=a.toDouble();
            double d3=d1+d2;
            QString S=QString::number(d3);
            ui->display->setText(S);
            Result=S;
            a="0";
        }
        if(op==2)
        {
            double d1=Result.toDouble();
            double d2=a.toDouble();
            double d3=d1-d2;
            QString S=QString::number(d3);
            ui->display->setText(S);
            Result=S;
            a="0";
        }
        if(op==3)
        {
            double d1=Result.toDouble();
            double d2=a.toDouble();
            double d3=d1*d2;
            QString S=QString::number(d3);
            ui->display->setText(S);
            Result=S;
            a="0";
        }
        if(op==4)
        {
            double d1=Result.toDouble();
            double d2=a.toDouble();
            if(d2!=0)
            {
                double d3=d1/d2;
                QString S=QString::number(d3);
                ui->display->setText(S);
                Result=S;
            }
            else
            {
               Dialog::on_C_clicked();
               ui->display->setText("!");
            }
            a="0";
        }

        Lock=true;
        hasCalculate=true;
    }
}

void Dialog::on_add_clicked()
{
    if(isResult==false)
    {
        isResult=true;
        op=1;
        Result=a;
        a="0";
    }
    else
    {
        if(!hasCalculate)
            Dialog::on_equal_clicked();
        op=1;
    }
}



void Dialog::on_sub_clicked()
{
    if(isResult==false)
    {
        isResult=true;
        op=2;
        Result=a;
        a="0";
    }
    else
    {
        if(!hasCalculate)
            Dialog::on_equal_clicked();
        else

        op=2;
    }
}

void Dialog::on_multiply_clicked()
{
    if(isResult==false)
    {
        isResult=true;
        op=3;
        Result=a;
        a="0";
    }
    else
    {
        if(!hasCalculate)
            Dialog::on_equal_clicked();
        op=3;
    }
}

void Dialog::on_divide_clicked()
{
    if(isResult==false)
    {
        isResult=true;
        op=4;
        Result=a;
        a="0";
    }
    else
    {
        if(!hasCalculate)
            Dialog::on_equal_clicked();
        op=4;
    }
}

void Dialog::on_spot_clicked()
{
    if(a.indexOf(".")==-1)
    {
        QString S=".";
        a+=S;
        ui->display->setText(a);
    }
}

void Dialog::on_reciprocal_clicked()
{
    double d=a.toDouble();
    if(d!=0)
    {
        d=1/d;
        a=QString::number(d);
        ui->display->setText(a);
        Lock=true;
    }
    else
    {
        if(Result==0)
        {
            Dialog::on_C_clicked();
            ui->display->setText("Can't be 0!");
        }
        else
        {
            d=Result.toDouble();
            d=1/d;
            a=QString::number(d);
            ui->display->setText(a);
            Lock=true;
        }
    }
}

void Dialog::on_square_clicked()
{
    double d=a.toDouble();
    d=d*d;
    a=QString::number(d);
    ui->display->setText(a);
    Lock=true;
}

void Dialog::on_sqrt_clicked()
{
    double d=a.toDouble();
    if(d>=0)
    {
        d=sqrt(d);
        a=QString::number(d);
        ui->display->setText(a);
        Lock=true;
    }
    else
    {
        Dialog::on_C_clicked();
        ui->display->setText("!");
    }
}
