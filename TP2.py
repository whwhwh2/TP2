def score(subject, student1, student2, student3,):
    subject,student1,student2,student3=['국어','수학','영어','과학','체육'],[],[],[]
    index_num=subject.index('국어')
    korean_sum=student1[index_num]+student2[index_num]+student3[index_num]
    korean_sum2=student1[index_num]+student2[index_num]+student3[index_num]/3

if __name__ == "__main__":
    main()