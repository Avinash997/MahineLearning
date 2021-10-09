function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returns the new centroids by computing the means of the 
%data points assigned to each centroid.
%   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
%   computing the means of the data points assigned to each centroid. It is
%   given a dataset X where each row is a single data point, a vector
%   idx of centroid assignments (i.e. each entry in range [1..K]) for each
%   example, and K, the number of centroids. You should return a matrix
%   centroids, where each row of centroids is the mean of the data points
%   assigned to it.
%

% Useful variables
[m n] = size(X);

% You need to return the following variables correctly.
centroids = zeros(K, n);
a = zeros(K , 1);
for i = 1:K
    a(i) = sum(idx == i) ;
end
for i = 1:m
    s = idx(i) ;
    centroids(s,:) = centroids(s,:) + X(i,:) ;
end
a = 1./a ;
for i = 1:n
centroids(:,i) = centroids(:,i) .* a ;

%   we can use the code below instead of code above //
%   for i=1:K
%   	s=find(idx==i);
%   	centroids(i,:)=mean(X(s,:));
%   end

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every centroid and compute mean of all points that
%               belong to it. Concretely, the row vector centroids(i, :)
%               should contain the mean of the data points assigned to
%               centroid i.
%
% Note: You can use a for-loop over the centroids to compute this.
%








% =============================================================


end

