def processFileToCSV(fileData, inputPath, outputPath):
    file = open(inputPath + fileData[0] + '.txt', 'r')
    result = open(outputPath + fileData[0] + '.csv', 'w')

    result.write(fileData[1])

    for line in file.readlines():
        result.write(line.replace(',', ';').replace('\t', ','))

    result.close()
    file.close()


if __name__ == "__main__":
    columnNamesClasses = "class,count\n"
    columnNamesGT = "series_episode,class,start,end,one_person_visible,atypical,shotcut,moving_camera,background,front,side,unusual_viewpoint,occlusion,truncation,beginning_missing,end_missing,comments\n"
    
    for fileData in [["classes", columnNamesClasses], ["GT-test", columnNamesGT], ["GT-train", columnNamesGT], ["GT-val", columnNamesGT]]:
        processFileToCSV(fileData, "../data/txt/", "../data/csv/")
