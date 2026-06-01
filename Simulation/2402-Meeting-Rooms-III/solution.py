class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        room_freq = defaultdict(int)
        # this tells how many rooms are available
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        # this tells how many rooms are occupied and when they are going to end
        occupied_rooms = []
        for st, end in meetings:
            # here we check any occupied rooms will be free to conduct this meeting
            while occupied_rooms and occupied_rooms[0][0] <= st:
                # here we only care about room no
                _, room_no = heapq.heappop(occupied_rooms)
                # this room is free, so we will add to the free_rooms list so we can use later
                heapq.heappush(free_rooms, room_no)
            # if we have free room,then go ahead take it and conduct the meeting
            if free_rooms:
                room_no = heapq.heappop(free_rooms)
                heapq.heappush(occupied_rooms, (end, room_no))
                room_freq[room_no] += 1
            # so if there are no free rooms, take the min(early ending meeting or (top of heap)) replace it with a delayed change
            else:
                endT, room_no = heapq.heappop(occupied_rooms)
                # delay change
                delay = end + (endT - st)
                # push it back to heap after replace and delay changes
                heapq.heappush(occupied_rooms, (delay, room_no))
                room_freq[room_no] += 1
        #then we find the maximum(freq) of a room
        res=max(room_freq.values())
        for key,val in room_freq.items():
            if(val==res):
                return key
