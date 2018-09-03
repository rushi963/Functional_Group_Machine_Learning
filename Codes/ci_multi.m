% Confidence Intervals
clear all;
close all;
clc;

ylim([45, 90]);
line([1 2],[88.11 88.11],'Color','r','LineWidth',2)
hold on
line([1 2],[84.71 84.71],'Color','r','LineWidth',2)
hold on
plot(1.5, 86.41, 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'r', 'LineWidth',2)
hold on
line([3 4],[77.15 77.15],'Color','r','LineWidth',2)
hold on
line([3 4],[57.40 57.40],'Color','r','LineWidth',2)
hold on
plot(3.5, 67.28, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'r', 'LineWidth',2)
line([1.5 1.5],[88.11 84.71],'Color','r','LineWidth',2)
hold on
line([3.5 3.5],[77.15 57.40],'Color','r','LineWidth',2)
hold on
str_title = ['MLP-1'];
tx = text(2,50,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

line([7 8],[88.26 88.26],'Color','b','LineWidth',2)
hold on
line([7 8],[85.17 85.17],'Color','b','LineWidth',2)
hold on
plot(7.5, 86.71, 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'LineWidth',2)
hold on
line([9 10],[75.09 75.09],'Color','b','LineWidth',2)
hold on
line([9 10],[64.27 64.27],'Color','b','LineWidth',2)
hold on
plot(9.5, 69.68, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'LineWidth',2)
line([7.5 7.5],[88.26 85.17],'Color','b','LineWidth',2)
hold on
line([9.5 9.5],[75.09 64.27],'Color','b','LineWidth',2)
hold on
str_title = ['MLP-2'];
tx = text(8,50,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

line([13 14],[87.76 87.76],'Color','g','LineWidth',2)
hold on
line([13 14],[84.01 84.01],'Color','g','LineWidth',2)
hold on
plot(13.5, 85.89, 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'g', 'LineWidth',2)
hold on
line([15 16],[73.21 73.21],'Color','g','LineWidth',2)
hold on
line([15 16],[62.28 62.28],'Color','g','LineWidth',2)
hold on
plot(15.5, 67.74, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'g', 'LineWidth',2)
line([13.5 13.5],[87.76 84.01],'Color','g','LineWidth',2)
hold on
line([15.5 15.5],[73.21 62.28],'Color','g','LineWidth',2)
hold on
str_title = ['SVM'];
tx = text(14,50,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

line([19 20],[80.01 80.01],'Color','m','LineWidth',2)
hold on
line([19 20],[74.99 74.99],'Color','m','LineWidth',2)
hold on
plot(19.5, 77.50, 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'm', 'LineWidth',2)
hold on
line([21 22],[65.22 65.22],'Color','m','LineWidth',2)
hold on
line([21 22],[53.15 53.15],'Color','m','LineWidth',2)
hold on
plot(21.5, 59.18, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'm', 'LineWidth',2)
line([19.5 19.5],[80.01 74.99],'Color','m','LineWidth',2)
hold on
line([21.5 21.5],[65.22 53.15],'Color','m','LineWidth',2)
hold on
str_title = ['KNN'];
tx = text(20,50,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

line([25 26],[83.20 83.20],'Color','k','LineWidth',2)
hold on
line([25 26],[78.58 78.58],'Color','k','LineWidth',2)
hold on
plot(25.5, 80.89, 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'k', 'LineWidth',2)
hold on
line([27 28],[69.89 69.89],'Color','k','LineWidth',2)
hold on
line([27 28],[59.68 59.68],'Color','k','LineWidth',2)
hold on
plot(27.5, 64.78, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'k', 'LineWidth',2)
line([25.5 25.5],[83.20 78.58],'Color','k','LineWidth',2)
hold on
line([27.5 27.5],[69.89 59.68],'Color','k','LineWidth',2)
hold on
str_title = ['RFC'];
tx = text(26,50,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

str_title = ['-  Multi Label Multiclass'];
tx = text(16,88,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

str_title = ['o Single Label Multiclass'];
tx = text(16,86,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

ylabel('10 Fold Accuracy (in %)', 'fontweight', 'bold', 'fontsize', 16);
%legend('o Intermediate Method', '- Complete Automation Approach')
%a=legend('O Intermediate Method', '- Complete Automation Approach', -1);
%b=findobj(a,'type','line','linestyle','-');
%set(b,'visible','off');