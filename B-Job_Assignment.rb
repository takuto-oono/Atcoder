def Jobs_Finish_Time(n, jobs_time)
    ans = 10000000
    for i in 0..n - 1
        for j in 0..n - 1
            if i == j
                ans = [ans, jobs_time[i][0] + jobs_time[j][1]].min
            else
                ans = [ans, [jobs_time[i][0], jobs_time[j][1]].max].min
            end
        end
    end
    return ans
end

n = gets.to_i
jobs_time = []
for i in 0..n - 1
    person_time = gets.split(' ').map(&:to_i)
    jobs_time.push(person_time)
end

ans = Jobs_Finish_Time(n, jobs_time)
puts ans


