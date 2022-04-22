h, w = gets.split(" ").map(&:to_i)
A = Array.new(h).map{Array.new(w, 0)}


for i in 0..h - 1 do
    a = gets.split(" ").map(&:to_i)
    for j in 0.. w - 1 do
        
        A[i][j] = a[j]
    end
    
end

x = A.flatten.min(1)

ans = 0
(0..h - 1).each do |i|
    (0..w - 1).each do |j|


        puts A[i][j] - x
    end

end


puts ans