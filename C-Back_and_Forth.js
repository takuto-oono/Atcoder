'use strict';





function main(input) {
    console.log('first');
    const [sx, sy, tx, ty] = input.split(' ').map(Number);
    const x = tx - sx;
    const y = ty - sy;
    console.log('test');
    const u = 'U';
    const r = 'R';
    const d = 'D';
    const l = 'L';

    let ans = '';
    ans += u.repeat(y) + r.repeat(x) + d.repeat(y) + l.repeat(x);
    ans += l + u.repeat(y + 1) + r.repeat(x + 1) + d;
    ans += r + d.repeat(y + 1) + l.repeat(x + 1) + u;

    
    

    
    console.log(ans);

}

main(require("fs").readFileSync("/dev/stdin", "utf8"));