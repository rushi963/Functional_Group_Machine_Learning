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
line([3 4],[68.92 68.92],'Color','r','LineWidth',2)
hold on
line([3 4],[62.53 62.53],'Color','r','LineWidth',2)
hold on
plot(3.5, 65.73, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'r', 'LineWidth',2)
line([1.5 1.5],[88.11 84.71],'Color','r','LineWidth',2)
hold on
line([3.5 3.5],[68.92 62.53],'Color','r','LineWidth',2)
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
line([9 10],[65.59 65.59],'Color','b','LineWidth',2)
hold on
line([9 10],[60.63 60.63],'Color','b','LineWidth',2)
hold on
plot(9.5, 63.11, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'LineWidth',2)
line([7.5 7.5],[88.26 85.17],'Color','b','LineWidth',2)
hold on
line([9.5 9.5],[65.59 60.63],'Color','b','LineWidth',2)
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
line([15 16],[68.47 68.47],'Color','g','LineWidth',2)
hold on
line([15 16],[63.46 63.46],'Color','g','LineWidth',2)
hold on
plot(15.5, 65.96, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'g', 'LineWidth',2)
line([13.5 13.5],[87.76 84.01],'Color','g','LineWidth',2)
hold on
line([15.5 15.5],[68.47 63.46],'Color','g','LineWidth',2)
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
line([21 22],[62.08 62.08],'Color','m','LineWidth',2)
hold on
line([21 22],[56.73 56.73],'Color','m','LineWidth',2)
hold on
plot(21.5, 59.40, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'm', 'LineWidth',2)
line([19.5 19.5],[80.01 74.99],'Color','m','LineWidth',2)
hold on
line([21.5 21.5],[62.08 56.73],'Color','m','LineWidth',2)
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
line([27 28],[71.24 71.24],'Color','k','LineWidth',2)
hold on
line([27 28],[67.13 67.13],'Color','k','LineWidth',2)
hold on
plot(27.5, 69.18, '+', 'MarkerSize', 6, 'MarkerEdgeColor', 'k', 'LineWidth',2)
line([25.5 25.5],[83.20 78.58],'Color','k','LineWidth',2)
hold on
line([27.5 27.5],[71.24 67.13],'Color','k','LineWidth',2)
hold on
str_title = ['RFC'];
tx = text(26,50,str_title);
tx.FontWeight = 'bold';
tx.FontSize = 12;

str_title = ['-  Intermediate Approach'];
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