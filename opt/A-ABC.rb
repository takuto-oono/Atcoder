k = gets.to_i

ans = 0
for i in 1..k
    j = 1
    while(i * j <= k) do
        ans += k / (i * j)
        j += 1
    end
end
puts ans